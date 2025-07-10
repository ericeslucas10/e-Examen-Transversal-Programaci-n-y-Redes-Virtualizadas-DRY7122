from ncclient import manager

router = {
    "host": "192.168.56.103",
    "port": 830,
    "username": "cisco",
    "password": "cisco123!"
}


config_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>Erices-vidal</hostname>
  </native>
</config>
"""

# Configuración de la Loopback11
config_loopback = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
      <Loopback>
        <name>11</name>
        <ip>
          <address>
            <primary>
              <address>11.11.11.11</address>
              <mask>255.255.255.255</mask>
            </primary>
          </address>
        </ip>
      </Loopback>
    </interface>
  </native>
</config>
"""

# Conexión NETCONF y aplicación de configuraciones
with manager.connect(**router, hostkey_verify=False) as m:
    print(" Conexión NETCONF establecida con", router["host"])

    print(" Cambiando hostname a 'Erices-vidal'...")
    response1 = m.edit_config(target='running', config=config_hostname)
    print(response1)

    print(" Creando Loopback11 con IP 11.11.11.11/32...")
    response2 = m.edit_config(target='running', config=config_loopback)
    print(response2)

    print(" Configuraciones aplicadas correctamente.")
