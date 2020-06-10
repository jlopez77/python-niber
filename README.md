# niber
I-DE daily data scrapper

Poor coded proof of concept on scrapping daily consumption data from Iberdrola I-DE website.
As I-DE API is blocked to automated querys with a catpcha, creative methods are needed.

This code will require dependencies like geckodriver, selenium and others not (yet) described here.
Use at your own risk.

Part of this code is borrowed from https://github.com/hectorespert/python-oligo/tree/master/oligo

fast usage:

  from niber import niber<br>
  connection = niber()<br>
  connection.login("username@mail.com","password")<br>
  watt = connection.watthourmeter()<br>
  print(watt)<br>
  consumo = connection.consumption()<br>
  print(consumo)<br>
