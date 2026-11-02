import exercise8_16_modul
exercise8_16_modul.describe_city('los angeles')

from exercise8_16_modul import describe_city
describe_city('san diego')

from exercise8_16_modul import describe_city as dc
dc('edinburgh', 'scotland')

import exercise8_16_modul as cf
cf.describe_city('los angeles')

from exercise8_16_modul import *
describe_city('san diego')