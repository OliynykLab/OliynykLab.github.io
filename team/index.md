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

{% include list.html data="members" component="portrait" filter="role == 'pi'" %}
{% include list.html data="members" component="portrait" filter="role == 'postdoc'" %}
{% include list.html data="members" component="portrait" filter="role == 'phd'" %}
{% include list.html data="members" component="portrait" filter="role == 'programmer'" %}
{% include list.html data="members" component="portrait" filter="role == 'undergrad'" %}

{% include section.html background="images/background.jpg" dark=true %}

{% capture content %}

{% endcapture %}

{% include grid.html style="square" content=content %}

## Alumni

{% include list.html data="members" component="portrait" filter="status == 'alumni'" %}