# muecke imports
import muecke.catalog.utils
from muecke.export.models import CategoryOption
from muecke.export.models import Export
from muecke.export.models import Script
from muecke.export.settings import CATEGORY_VARIANTS_DEFAULT
from muecke.export.settings import CATEGORY_VARIANTS_CHEAPEST
from muecke.export.settings import CATEGORY_VARIANTS_ALL


def register(method, name):
    """Registers a new export logic.
    """
    try:
        Script.objects.get(
            module=method.__module__, method=method.__name__)
    except Script.DoesNotExist:
        try:
            Script.objects.create(
                module=method.__module__, method=method.__name__, name=name)
        except:
            # Fail silently
            pass
    except:
        # Fail silently
        pass


def get_variants_option(export, product):
    """Returns the variants option for given category or None.
    """
    try:
        category = product.get_categories()[0]
    except IndexError:
        return None

    while category:
        try:
            category_option = CategoryOption.objects.get(
                export=export, category=category)
        except:
            category = category.parent
        else:
            return category_option.variants_option
    return None


def get_variants(product, export):
    """Returns the variants for given product and export.
    """
    variants_option = get_variants_option(export, product)
    if variants_option is None:
        variants_option = export.variants_option

    if variants_option == CATEGORY_VARIANTS_DEFAULT:
        if product.get_default_variant():
            return [product.get_default_variant()]
        else:
            return []
    elif variants_option == CATEGORY_VARIANTS_ALL:
        return product.get_variants()
    elif variants_option == CATEGORY_VARIANTS_CHEAPEST:
        variants = list(product.get_variants())
        variants.sort(lambda a, b: cmp(a.get_price(), b.get_price()))
        try:
            return [variants[0]]
        except IndexError:
            return []
