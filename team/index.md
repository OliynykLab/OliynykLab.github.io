---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team

<div style="text-align: center;">
  Here's our wonderful team!
</div>

{% include section.html %}

## Principal Investigator (PI)

{% include list.html data="members" component="portrait" filter="role == 'pi'" %}

## Postdocs

{% include list.html data="members" component="portrait" filter="role == 'postdoc'" %}

## PhD Students

{% include list.html data="members" component="portrait" filter="role == 'phd'" %}

## Postbacs

{% include list.html data="members" component="portrait" filter="role == 'postbac'" %}

## Research Volunteers

{% include list.html data="members" component="portrait" filter="role == 'programmer'" %}

## Undergraduates

{% include list.html data="members" component="portrait" filter="role == 'undergrad'" %}

{% include section.html background="images/background.jpg" dark=true %}

{% capture content %}

{% endcapture %}

{% include grid.html style="square" content=content %}

## High-schoolers

[TBA]

## Alumni

{% include list.html data="members" component="portrait" filter="status == 'alumni'" %}
