from rest_framework.views import APIView
from rest_framework.response import Response
from .models import FactoryModel, ProductMaterialModel, WarehousesModel


class ProductMaterialData(APIView):
    def get(self, request, format=None):
        factories = FactoryModel.objects.all()
        warehouse = WarehousesModel.objects.all()
        counter = {}
        total_dict = {}
        result = []

        for w in warehouse:
            if w.material.material not in counter.keys():
                counter[w.material.material] = 0
            total_dict.setdefault(w.material.material,0)
            total_dict[w.material.material] += w.remainder



        for factory in factories:
            product_materials = ProductMaterialModel.objects.filter(
                product=factory.product
            )
            product_material = []
            for m in product_materials:
                if m.product.product_name == factory.product.product_name:
                    total_sum = 0
                    for w in warehouse:
                        if w.material.material == m.raw_material.material:
                            if (w.remainder - (m.quantity * factory.product_count-total_sum)) <= 0:
                                if counter[w.material.material] < w.remainder:
                                    counter[w.material.material] += w.remainder
                                    total_sum += w.remainder
                                    product_material.append(
                                        {
                                            "warehouse": w.id,
                                            "material_name": w.material.material,
                                            "qty": int(w.remainder),
                                            "price": w.price,
                                        }
                                    )
                                elif counter[w.material.material] <= w.remainder:
                                    if total_dict[w.material.material]-w.remainder > 0:
                                        product_material.append(
                                            {
                                                "warehouse": w.id,
                                                "material_name": w.material.material,
                                                "qty": int(total_dict[w.material.material]-w.remainder),
                                                "price": w.price,
                                            }
                                        )
                                        product_material.append(
                                             {
                                                 "warehouse": None,
                                                 "material_name": w.material.material,
                                                 "qty": int(w.remainder-(total_dict[w.material.material]-w.remainder)),
                                                 "price": None,
                                             }
                                        )
                            else:
                                counter[w.material.material] += w.remainder-((w.remainder + total_sum)-(m.quantity * factory.product_count))
                                product_material.append(
                                    {
                                        "warehouse": w.id,
                                        "material_name": w.material.material,
                                        "qty": int(w.remainder-((w.remainder + total_sum)-(m.quantity * factory.product_count))),
                                        "price": w.price,
                                    }
                                )
                                total_sum = 0
            result.append(
                {
                    "product_name": factory.product.product_name,
                    "product_qty": factory.product_count,
                    "product_materials": product_material,
                }
            )
        print(counter)
        ctx = {
            "result": result,
        }
        
        return Response(ctx)
