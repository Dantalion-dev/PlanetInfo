def run():
  from packages.classeA import Astronomy
  from packages.classeB import sargs

  args = sargs()
  Astronomy = Astronomy(args)
  url  = Astronomy.planet_info()
  code = Astronomy.request(url)
  Astronomy.filter(code)
