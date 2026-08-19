import json
from urllib.request import Request, urlopen
from util import *


def main(entry):
    """
    receives single list entry from orcid data file
    returns list of sources to cite
    """

    # orcid api
    endpoint = "https://pub.orcid.org/v3.0/$ORCID/works"
    headers = {"Accept": "application/json"}

    # get id from entry
    _id = get_safe(entry, "orcid", "")
    if not _id:
        raise Exception('No "orcid" key')

    # query api
    @log_cache
    @cache.memoize(name=__file__, expire=1 * (60 * 60 * 24))
    def query(_id):
        url = endpoint.replace("$ORCID", _id)
        request = Request(url=url, headers=headers)
        response = json.loads(urlopen(request).read())
        return get_safe(response, "group", [])

    response = query(_id)

    # list of sources to return
    sources = []

    # go through response structure and pull out ids e.g. doi:1234/56789
    for work in response:
        # get list of ids
        ids = []
        for summary in get_safe(work, "work-summary", []):
            ids = ids + get_safe(summary, "external-ids.external-id", [])

        # find first id of particular "relationship" type
        _id = next(
            (
                id
                for id in ids
                if get_safe(id, "external-id-relationship", "")
                in ["self", "version-of", "part-of"]
            ),
            ids[0] if len(ids) > 0 else None,
        )

        if _id == None:
            continue

        # get id and id-type from response
        id_type = get_safe(_id, "external-id-type", "")
        id_value = get_safe(_id, "external-id-value", "")

        # create source
        source = {"id": f"{id_type}:{id_value}"}

        # Keep ORCID's summary metadata for every work. Manubot enriches it when
        # available, while these fields make the publication usable if it is not.
        summaries = get_safe(work, "work-summary", [])

        def first(get_func):
            return next((value for value in map(get_func, summaries) if value), None)

        title = first(lambda s: get_safe(s, "title.title.value", ""))
        publisher = first(lambda s: get_safe(s, "journal-title.value", ""))
        link = first(lambda s: get_safe(s, "url.value", ""))
        publication_date = first(lambda s: get_safe(s, "publication-date", {})) or {}
        year = get_safe(publication_date, "year.value", "")
        month = get_safe(publication_date, "month.value", "01")
        day = get_safe(publication_date, "day.value", "01")

        if title:
            source["title"] = title
        if publisher:
            source["publisher"] = publisher
        if year:
            source["date"] = f"{year}-{str(month).zfill(2)}-{str(day).zfill(2)}"
        if link:
            source["link"] = link
        elif id_type == "doi" and id_value:
            source["link"] = f"https://doi.org/{id_value}"

        # copy fields from entry to source
        source.update(entry)

        # add source to list
        sources.append(source)

    return sources
