[![GitHub release](https://img.shields.io/github/release/JiriKursky/Indego.svg)](https://GitHub.com/JiriKursky/Indego_350/releases/) 

# Indego_350
Home Assistant Custom Component for Bosch Indego Lawn Mower.
<p>Adding sensor for position of mower and services for display mower in map 
<hr>


## Installation

Create in your Homeassistant directory `/config/custom_components/indego_map`.
Copy the folder `custom/components/indego_map` into your  your Home Assistant `/config/custom_components/indego_map`.

How to install: [Tutorial](https://appframework.readthedocs.io/en/latest/INDEGO_MOWER.html#tutorial)

## Reboot
Reboot HA in order to get HA to find the newly added custom component.

## Configuration
Add the domain to your configuration.yaml. Username, password and id (serial) is mandatory. Name (default = Indego) and polling (default = false) is optional.
``` yaml
#configuration.yaml
indego_map:
#Required
  username: !secret indego_username
  password: !secret indego_password
  id:       !secret indego_id
#Optional
  name:     Indego
```

Add your credentials used with Bosch Mower app (mail address, password and mower serial number) to your secrets.yaml: 
``` yaml
#secrets.yaml
indego_username: "name@mail.com"
indego_password: "mysecretpw"
indego_id:       "123456789"
```
## Usage

For displaying map you will need [AppDaemon](https://appdaemon.readthedocs.io/en/latest/) and [AppFramework](https://appframework.readthedocs.io/en/latest/index.html). 
In AppFramework you will also find tutorial how to set up map in lovelace.


![Map example](/images/m1-map.png)



## Credits

Base of component is copied from [jm-73](https://github.com/jm-73/Indego)

### Thanks to
[Eduard](https://github.com/eavanvalkenburg)
[Jumper78](https://github.com/Jumper78)
[dykandDK](https://github.com/dykandDK)
[ultrasub](https://github.com/UltraSub)
[Gnol86](https://github.com/Gnol86)
naethan bekkm onkelfarmor ltjessem nsimb jjandersson
[Shamshala](https://github.com/Shamshala)
nath
[bekkm](https://github.com/bekkm)
[urbatecte](https://github.com/urbatecte)

Inspiration from http://grauonline.de/wordpress/?page_id=219

Inspiration from https://github.com/jofleck/iot-device-bosch-indego-controller

