const BASE = '/laboratorios/api/';

const bacteriologos = BASE.concat('bacteriologos/');
const caracteristicas = BASE.concat('caracteristicas/');
const equipos = BASE.concat('equipos/');
const especificacion_caracteristicas = BASE.concat('especificacion_caracteristicas/');
const especificaciones_por_carateristica = BASE.concat('especificacion_caracteristicas/caracteristica/');
const formatos = BASE.concat('formatos/');
const laboratorios = BASE.concat('laboratorios/');
const ordenes_laboratorios = BASE.concat('ordenes_laboratorios/');
const reactivos = BASE.concat('productos/');
const secciones_trabajo = BASE.concat('seccion_trabajo/');
const plantillaArea = BASE.concat('seccion_trabajo/plantillas/');
const plantillaLaboratorio = BASE.concat('laboratorios/plantilla_laboratorios/');
const tecnicas = BASE.concat('tecnicas/');
const servicios = BASE.concat('servicios/');
const resultados = BASE.concat('resultado/');
const ordenes_busqueda = BASE.concat('ordenes/buscar/');
const laboratoriosTomaMuestra = BASE.concat('ordenes/toma_muestra/');
const plantillasOrdenes = BASE.concat('laboratorios/plantilla/');


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
    plantillaLaboratorio
}
