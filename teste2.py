
from configparser import ConfigParser
import os

caminhoConfig= 'C:\\projetos\\datavix\\robo\\digitadorIN\\config.ini'
print(caminhoConfig)
caminhoConfig = os.path.abspath(os.path.join(os.path.dirname(__file__), "config.ini"))
print(caminhoConfig)
caminhoConfig = os.path.join(os.path.dirname(__file__), "config.ini")
print(caminhoConfig)

#ARRAffinity="4158b8cb52670287f6c8ed527deabcf61e852bbce20c1d69134187e490db1687	"
#SessionID="kt2z4ur1f0tb3pxg1et5rjvo		"
#Aspxauth="A377ADE28E10D3FAF8CD1E5C7B22D0B1632F597A238C8551B0670914D0361736857721638E866639B413DB72FE7AE818645D7613A60F106C8FDBAB64252FE5EC97CC1F19D6487A9B7EB55A1377E01F9C60011D6A95788307B9B08E1ED6139889A92921B49075D05AECB2083C0BC71BB41FA0B39724736CF5E8521EDEE27EE4F51763BEC23BEEEAB311162E84C3D0A1B6AE1373349EBA74D9F3784A0BE738E7CE59B582D8C4581A590E552D027E7EE828		"

config = ConfigParser()
#config.read('config.ini')
#print(config.get("default","ARRAffinity"))
#print(config.get("default","SessionID"))
#print(config.get("default","Aspxauth"))

config.write('config.ini')
config.add_section("default")
config.set("default", "ARRAffinity", "tst1")
config.set("default", "SessionID", "tst2")
config.set("default", "Aspxauth", "tst3")
file = open("config.ini", "w")
config.write(file)
file.close()
