#_____                                      _               ______                                              _           _   _                  
#|  __ \                                    | |              | ___ \                                            | |         | | | |                 
#| |  \/  ___  _ __    ___  _ __   __ _   __| |  ___   _ __  | |_/ /  __ _  ___  ___ __      __  ___   _ __   __| |   ___   | | | | ___   ___  _ __ 
#| | __  / _ \| '_ \  / _ \| '__| / _` | / _` | / _ \ | '__| |  __/  / _` |/ __|/ __|\ \ /\ / / / _ \ | '__| / _` |  / _ \  | | | |/ __| / _ \| '__|
#| |_\ \|  __/| | | ||  __/| |   | (_| || (_| || (_) || |    | |    | (_| |\__ \\__ \ \ V  V / | (_) || |   | (_| | | (_) | | |_| |\__ \|  __/| |   
# \____/ \___||_| |_| \___||_|    \__,_| \__,_| \___/ |_|    \_|     \__,_||___/|___/  \_/\_/   \___/ |_|    \__,_|  \___/   \___/ |___/ \___||_|   
                                                                                                                                                   
                                                                                                                                                   
                                                                                                                                              
                                                                                                                                                   
import random

lower = "abcdefghijklmnñopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
number = "0123456789"
symbols = ".-*#$&%"
all = lower+upper+number+symbols
length=20
password = "".join(random.sample(all,length))
print(password)