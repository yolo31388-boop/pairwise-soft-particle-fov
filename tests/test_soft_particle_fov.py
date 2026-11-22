import pytest
import render.soft_particle_fov as mod

CASES = [
    ("view_space_depth", (1, 2)),
    ("fov_normalize", (60.0, 90.0)),
    ("fade_width_ratio", (0.1, 0.2)),
    ("hard_clip_detect", (1, 2)),
    ("aspect_guard", (1, 2)),
    ("depth_texture", (1, 2)),
    ("fade_curve", (1.0, 2.0)),
    ("near_plane", (0.1, 0.2)),
    ("particle_sort", (1, 2)),
    ("blending_mode", (1, 2)),
    ("fallback_linear", (1, 2)),
    ("edge_softness", (0.5, 0.2)),
    ("validation", (1, 2)),
    ("fov_metric", (1.0, 2.0)),
    ("batch_guard", (1, 2)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
