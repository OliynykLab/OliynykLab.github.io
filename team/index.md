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

{% include button.html icon="fa-solid fa-door-open" text="Join us!" link="/team/join" %}

{% include section.html %}

## Principal Investigator

{% include list.html data="members" component="portrait" filter="role == 'pi'" %}

## Postdocs

{% include list.html data="members" component="portrait" filter="role == 'postdoc'" %}

## PhD Students

{% include list.html data="members" component="portrait" filter="role == 'phd' and status != 'alumni'" %}

## Students & Volunteers

{% include list.html data="members" component="portrait" filter="role == 'postbac' and status != 'alumni'" %}
{% include list.html data="members" component="portrait" filter="role == 'programmer' and status != 'alumni'" %}
{% include list.html data="members" component="portrait" filter="role == 'undergrad' and status != 'alumni'" %}

## High-schoolers

{% include list.html data="members" component="portrait" filter="role == 'Highschooler' and status != 'alumni'" %}

{% capture content %}

{% endcapture %}

{% include grid.html style="square" content=content %}

## Alumni

{% include list.html data="members" component="portrait" filter="status == 'alumni'" %}
