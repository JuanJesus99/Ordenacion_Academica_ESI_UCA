
import ldap



def conectar_ldap(user, password):
    print("Usuario: "+user+" y Contraseña: "+password)
      
    ldapHost = "ldap://ldap.uca.es"
    LDAP_BASE_DN = "CN="+user+",dc=uca,dc=es"
    LDAP_ATTRS = ["mail", "ou"]
    ldap_filter = "tipodocumento=NIF"
    
    loginDN = "CN="+user+",dc=uca,dc=es"
    # ldapPort = 389
    
    try:
        ldap_client = ldap.initialize(ldapHost)
        ldap_client.set_option(ldap.OPT_PROTOCOL_VERSION,3)
        ldap_client.simple_bind_s(loginDN,password)
    except ldap.INVALID_CREDENTIALS:
        print("Wrong username or password.")
        ldap_client.unbind()
    except ldap.SERVER_DOWN:
        print("LDAP server not available")

    user_info = ldap_client.search_s(LDAP_BASE_DN, ldap.SCOPE_BASE, ldap_filter, LDAP_ATTRS)

    print(user_info)