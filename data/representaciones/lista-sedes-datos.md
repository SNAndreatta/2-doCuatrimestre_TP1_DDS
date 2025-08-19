# Estructura de `lista-sedes.csv`

## Versión extendida de lista-secciones

### Campos

#### Identificación
- **sede_id** → Identificador único de la sede.  
- **sede_desc_castellano** → Nombre de la sede en castellano.  
- **sede_desc_ingles** → Nombre de la sede en inglés.  

#### País
- **pais_castellano** → Nombre del país en castellano.  
- **pais_ingles** → Nombre del país en inglés.  
- **region_geografica** → Región geográfica donde se ubica el país (ej. *América del Sur*, *Europa Occidental*).  
- **pais_iso_2** → Código de país ISO de 2 letras.  
- **pais_iso_3** → Código de país ISO de 3 letras.  
- **pais_codigo_telefonico** → Prefijo telefónico internacional del país.  

#### Ciudad
- **ciudad_castellano** → Nombre de la ciudad en castellano.  
- **ciudad_ingles** → Nombre de la ciudad en inglés.  
- **ciudad_zona_horaria_gmt** → Zona horaria de la ciudad en relación a GMT (ej. `GMT-3`).  
- **ciudad_codigo_telefonico** → Prefijo telefónico de la ciudad.  

#### Estado
- **estado** → Estado de la sede (ej. *Activo*, *Cerrado*).  

#### Titular
- **titular_nombre** → Nombre del titular de la sede.  
- **titular_apellido** → Apellido del titular.  
- **titular_cargo** → Cargo del titular (ej. *Embajador*, *Cónsul General*).  

#### Dirección
- **direccion** → Dirección física de la sede.  
- **codigo_postal** → Código postal de la dirección.  

#### Contacto telefónico
- **telefono_principal** → Número de teléfono principal.  
- **telefonos_adicionales** → Lista de teléfonos adicionales separados por `" // "`.  
- **celular_guardia** → Número de celular para guardias o emergencias.  
- **celulares_adicionales** → Lista de celulares adicionales separados por `" // "`.  
- **fax_principal** → Fax principal de la sede.  
- **faxes_adicionales** → Lista de faxes adicionales separados por `" // "`.  

#### Correo electrónico
- **correo_electronico** → Correo electrónico principal.  
- **correos_electronicos_adicionales** → Correos electrónicos adicionales separados por `" // "`.  

#### Web y redes
- **sitio_web** → Página web oficial de la sede.  
- **sitios_web_adicionales** → Lista de sitios web adicionales separados por `" // "`.  
- **redes_sociales** → Lista de redes sociales de la sede, separadas por `" // "`.  

#### Horarios de atención
- **atencion_dia_desde** → Día de la semana de inicio de atención.  
- **atencion_dia_hasta** → Día de la semana de fin de atención.  
- **atencion_hora_desde** → Hora de apertura.  
- **atencion_hora_hasta** → Hora de cierre.  
- **atencion_comentario** → Observaciones adicionales sobre el horario (ej. “No se atiende feriados”).  

#### Otros
- **concurrencias** → Lista de países/regiones adicionales donde la sede también tiene competencia consular o diplomática.  
- **circunscripcion** → Delimitación geográfica específica donde la sede tiene jurisdicción.  
