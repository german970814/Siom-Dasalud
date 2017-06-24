const BASE = '/laboratorios/api/';

const bacteriologos = BASE.concat('bacteriologos/');
const caracteristicas = BASE.concat('caracteristicas/');
const empleados = BASE.concat('empleados/');
const equipos = BASE.concat('equipos/');
const especificacion_caracteristicas = BASE.concat('especificacion_caracteristicas/');
const especificaciones_por_carateristica = BASE.concat('especificacion_caracteristicas/caracteristica/');
const formatos = BASE.concat('formatos/');
const laboratorios = BASE.concat('laboratorios/');
const laboratoriosTomaMuestra = BASE.concat('ordenes/toma_muestra/');
const ordenes_busqueda = BASE.concat('ordenes/buscar/');
const ordenes_laboratorios = BASE.concat('ordenes_laboratorios/');
const plantillaArea = BASE.concat('seccion_trabajo/plantillas/');
const plantillaLaboratorio = BASE.concat('laboratorios/plantilla_laboratorios/');
const plantillasOrdenes = BASE.concat('laboratorios/plantilla/');
const reactivos = BASE.concat('productos/');
const resultados = BASE.concat('resultado/');
const secciones_trabajo = BASE.concat('seccion_trabajo/');
const servicios = BASE.concat('servicios/');
const tecnicas = BASE.concat('tecnicas/');


export default {
    BASE,
    equipos,
    laboratorios,
    secciones_trabajo,
    tecnicas,
    reactivos,
    caracteristicas,
    especificacion_caracteristicas,
    ordenes_laboratorios,
    servicios,
    especificaciones_por_carateristica,
    formatos,
    bacteriologos,
    resultados,
    ordenes_busqueda,
    laboratoriosTomaMuestra,
    plantillaArea,
    plantillasOrdenes,
    plantillaLaboratorio,
    empleados
}
