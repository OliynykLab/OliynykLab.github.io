---
title: Projects
nav:
  order: 2
  tooltip: Software, datasets, and more
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects

<div style="text-align: center;">
Here's a list of some things we did! Most if not all of our software is open-source.
</div>

{% include tags.html tags="publication, resource, website, software" %}

{% include search-info.html %}

{% include section.html %}

## Featured

{% include list.html component="card" data="projects" filter="group == 'featured'" columns="4" %}

{% include section.html %}

## More

{% include list.html component="card" data="projects" filter="!group" style="small" %}

