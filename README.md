# pi-ds18b20-grafana

THIS IS A WORK IN PROGRESS

Description
- The purpose of this is to be able to graph multiple ds18b20 temperature probes connected to a Raspberry Pi.
- Currently, my setup involves two separately running python scripts that run at reboot via cron.
- Use the two t#-logger.py scripts as templates. Some things will have to be changed to fit your own setup (such as the w1 identifiers).

Logger Scripts
- I lost the original link to where I found this python script. Once I find it again, i'll credit the original author since this is not my own work.





### "t*_logger.py" scripts and "t*-watchdog" scripts should all be installed in /usr/bin and make them executable with chmod +x ###

Watchdog Scripts
- scripts came from here... https://stackoverflow.com/questions/696839/how-do-i-write-a-bash-script-to-restart-a-process-if-it-dies
- each sensor must have its own script

PREREQUISITES

1-wire must be enabled from raspi-config>interface options

###
"bc" package must be installed
  apt install bc

###
"influxdb" python module must be installed
  pip install influxdb

###
https://gpiozero.readthedocs.io/en/stable/remote_gpio.html

Also, don't forget to set your locale to US and US Keyboard and timezone as UTC in raspi-config...otherwise you'll be wondering where the hell your data is...
