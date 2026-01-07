
temperature = property(get_temperature,set_temperature)

# make empty property
temperature = property()

# assign fget
temperature = temperature.getter(get_temperature)

# assign fset
temperature = temperature.setter(set_temperature)
