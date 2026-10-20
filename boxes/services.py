SAFETY_MARGIN_CM = 2

def find_best_box(total_length, total_width, total_height, total_weight, boxes):
    product_dims = sorted([
        total_length + SAFETY_MARGIN_CM,
        total_width + SAFETY_MARGIN_CM,
        total_height + SAFETY_MARGIN_CM,
    ])
    eligible = []
    for box in boxes:
        box_dims = sorted([box.internal_length, box.internal_width, box.internal_height])
        fits = all(p <= b for p, b in zip(product_dims, box_dims))
        weight_ok = total_weight <= box.max_weight
        if fits and weight_ok:
            box_vol = box.internal_length * box.internal_width * box.internal_height
            product_vol = total_length * total_width * total_height
            wasted = box_vol - product_vol
            eligible.append((box, wasted))

    if not eligible:
        return None
    eligible.sort(key=lambda pair: (pair[1], pair[0].cost))
    return eligible[0][0]