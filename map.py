#!/usr/bin/env python3

"""."""
# pylint: disable=invalid-name

from pyvis.network import Network
import yaml


net = Network(width=1880, height=920)
net.force_atlas_2based(gravity=-100, spring_length=250, spring_strength=0.15, central_gravity=0.005)

source = open('map.yaml', 'r')
infra_map = yaml.load(source)

for key, value in infra_map.items():
    if value is None:
        value = []

    net.add_node(
        key,
        label='{}'.format(key),
        title='<b>{}</b>'.format(key)
    )

for key, value in infra_map.items():
    if key.endswith('-leaf'):
        net.add_edge('core1-master', key)
    else:
        net.add_edge(key[0:key.find("-")] + '-leaf', key)

net.toggle_physics(True)
# net.show_buttons(filter_=['physics'])
net.write_html('overview.html')
