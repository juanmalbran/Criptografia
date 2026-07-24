from psec import tr31


def importar():
    """Importa y muestra información de un Key Block TR-31"""
    kbpk_b = bytes.fromhex("A1A10101010101010101010101010103")
    kb_string = "D0144C0AB00S0000D67DB4180E4D545999D0874FADF8A8BE4319D062528246EF52E4FE90FA59A82E2E0813BDDAA2FF112A5B511D2E304185D8DB0ECCE4FF9110719ADDE054DFCCD8"
    
    # Crear KeyBlock con el KBPK
    kb = tr31.KeyBlock(kbpk_b)
    
    # Cargar el header desde el Key Block string
    kb.header.load(kb_string)
    
    # Unwrappear la clave
    clave_unwrapped = kb.unwrap(kb_string)
    
    print("=" * 60)
    print("INFORMACIÓN DEL KEY BLOCK TR-31")
    print("=" * 60)
    print(f"Clave importada (hex):  {clave_unwrapped.hex().upper()}")
    print(f"Versión:                {kb.header.version_id}")
    print(f"Uso de clave:           {kb.header.key_usage}")
    print(f"Algoritmo:              {kb.header.algorithm}")
    print(f"Modo de uso:            {kb.header.mode_of_use}")
    print(f"Exportabilidad:         {kb.header.exportability}")
    print(f"Número de versión:      {kb.header.version_num}")
    print("=" * 60)


def exportar():
    """Exporta una clave en formato TR-31"""
    # Construir header
    h = tr31.Header()
    h.version_id = "D"
    h.key_usage = "C0"
    h.algorithm = "A"
    h.mode_of_use = "B"
    h.exportability = "S"
    h.version_num = "00"
    
    # Claves
    kbpk = bytes.fromhex("A1A10101010101010101010101010103")
    key = bytes.fromhex("A2A1C1C1C1C1C1C1C1C1C1C1C1C1C1C2")
    
    # Crear Key Block y wrappear
    kb = tr31.KeyBlock(kbpk, h)
    key_block_wrapped = kb.wrap(key)
    
    print("=" * 60)
    print("EXPORTACIÓN TR-31")
    print("=" * 60)
    print(f"Key Block: {key_block_wrapped}")
    print("=" * 60)


if __name__ == "__main__":
    importar()
#    print("\n")
    exportar()