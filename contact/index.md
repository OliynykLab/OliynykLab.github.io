---
title: Contact
nav:
  order: 6
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

<div style="text-align: center;">
Questions? Want to collaborate or just reach out? Click below!
</div>

{%
  include button.html
  type="email"
  text="ao3014@hunter.cuny.edu"
  link="ao3014@hunter.cuny.edu"
%}

{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://g.co/kgs/GHvw54k"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/huntercollege.jpg"
  caption="Street view of Hunter!"
%}

{% endcapture %}

{% include cols.html col1=col1 %}

{% include section.html dark=true %}
