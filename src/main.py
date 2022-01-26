from pyfiglet import Figlet

# Heading
print(Figlet(font='slant').renderText('Dilute Acid'))


concentration1 = (float)(input("[?] Current concentration of ACID (in %): "))
concentration2 = (float)(input("[?] Required concentration of ACID (in %): "))
volume = (float)(input("[?] Required volume of diluted ACID (in ml): "))

acidVolumeRequired = concentration2 * volume / concentration1
waterVolumeRequired = volume - acidVolumeRequired

print(f"\n>> {round(waterVolumeRequired, 1)}ml H₂O + {round(acidVolumeRequired, 1)}ml {concentration1}% ACID = {round(volume, 1)}ml {concentration2}% ACID")
