from django import template

from ..utils import DictToObject

register = template.Library()


@register.filter
def get_resultado(instance, genero):
    """Funcion para mostrar los resultados en la tabla de resultados de la impresion de un laboratorio."""

    instance = DictToObject(instance)
    tipo = instance.tipo.name
    if tipo in ['number', 'text', 'textarea']:
        result = instance.model_text
        if tipo == 'number':
            number = float(result)
            if instance.referencias[genero.upper()]['minima'] and instance.referencias[genero.upper()]['minima']:
                result = '* %.2f' % number if number <= float(instance.referencias[genero.upper()]['minima']) or \
                    number >= float(instance.referencias[genero.upper()]['maxima']) else '%.2f' % number
            else:
                result = '%.2f' % number
            result += ' {}'.format(instance.unidades)
        else:
            result = result.upper()
    elif tipo == 'select':
        result = instance.model_text.text.upper()
    return result
