--Asegure el uso de la base de datos

use datos_sistema_turno

-- Ejecute lo siguiente para la confirmacion de almacenado en la base de datos

insert into formulario (id, Nombre, Apellido, tipo_cita, tratado_cita, fecha_cita , total_sin_itebis, Valor_itebis, total_con_itebis)
values('234','mary','feliz','2','Atencion al cliente','12/3/2022 ','650','117.0','767.0')



--Si desea eliminar todos los registros de la tabla ejecute lo siguiente 


delete from formulario





--Si desea visualizar todos los registros de la tabla ejecute lo siguiente 


select * from formulario