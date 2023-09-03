# ArevaloFlorencia-Comision55630

Nombre: Florencia Arevalo
Trabajo Final

Se desarrolla una app para el modelo de negocios de una empresa que precisa registrar y visualizar los datos de sus inversiones en un solo lugar. 
Por lo general, las empresas tienen inversiones en distintos bancos o Brokers, la idea sería que a través de esta aplicación puedan administrarlas desde un mismo sitio. 

Modelos (se indican con * al inicio, los atributos): 

- Fci: 
	* Nombre
  * Nomenclatura
  * Cuotapartes
  * Último valor
  * Fecha actualización
 
- Acciones: 
	* Nombre
  * Nomenclatura
  * Nominales
  * Fecha de inicio
 
Además, en este modelo podrán verse los gráficos de las acciones ingresadas vinculadas con la API de Yahoo Finance. 

- Bonos: 
	* Nombre
  * Nomenclatura
  * Nominales
  * Último valor
  * Fecha actualización
 
- Cauciones: 
	* Nombre
  * Nomenclatura
  * Nominales
  * Último valor
  * Fecha actualización

En cada página pueden buscarse los activos que se necesiten usando como patrón de búsqueda al nombre.

En cada página se pueden agregar, editar o borrar registros. 

El usuario podrá acceder únicamente si está registrado; en caso de no estarlo, al inicio tendrá la posibilidad de registrarse.

Se utilizó Class Based View para crear Login, Logout, Edición de perfiles, y CRUD de cada modelo. 



Para acceder a ADMIN:

Los datos del superuser son:
usuario: admin
contrasena:1234

Se creó otro usuario de prueba:
usuario: farevalo92
contrasena:Fl0r3nc14

