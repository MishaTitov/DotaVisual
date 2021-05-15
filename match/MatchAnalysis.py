import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt

file = open("match.json", )
data = json.load(file)
file.close()

fname = open("hero_names.json", )
dname = json.load(fname)
fname.close()

pls = np.array(data["players"])
radiant_pls = np.array(pls[:5])
for r_pl in radiant_pls:
    i = 0
    while (r_pl['hero_id'] != dname[i]['id']) or (i > 120):
        i = i + 1
    r_pl['localized_name'] = dname[i]['localized_name']

dire_pls = np.array(pls[5:])
for d_pl in dire_pls:
    i = 0
    while (d_pl['hero_id'] != dname[i]['id']) or (i > 120):
        i = i + 1
    d_pl['localized_name'] = dname[i]['localized_name']

x = np.arange(0, len(radiant_pls[0]['gold_t']))

fig = plt.figure()
ax_radiant = fig.add_subplot(2, 1, 1)
ax_radiant.plot(x, radiant_pls[0]['gold_t'], label=radiant_pls[0]['localized_name'])
ax_radiant.plot(x, radiant_pls[1]['gold_t'], label=radiant_pls[1]['localized_name'])
ax_radiant.plot(x, radiant_pls[2]['gold_t'], label=radiant_pls[2]['localized_name'])
ax_radiant.plot(x, radiant_pls[3]['gold_t'], label=radiant_pls[3]['localized_name'])
ax_radiant.plot(x, radiant_pls[4]['gold_t'], label=radiant_pls[4]['localized_name'])
ax_radiant.grid()
ax_radiant.set_xticks(np.arange(np.min(x), np.max(x), 4))
ax_radiant.set_xlabel("time in minutes")
ax_radiant.legend()

ax_dire = fig.add_subplot(2, 1, 2)
ax_dire.plot(x, dire_pls[0]['gold_t'], label=dire_pls[0]['localized_name'])
ax_dire.plot(x, dire_pls[1]['gold_t'], label=dire_pls[1]['localized_name'])
ax_dire.plot(x, dire_pls[2]['gold_t'], label=dire_pls[2]['localized_name'])
ax_dire.plot(x, dire_pls[3]['gold_t'], label=dire_pls[3]['localized_name'])
ax_dire.plot(x, dire_pls[4]['gold_t'], label=dire_pls[4]['localized_name'])
ax_dire.grid()
ax_dire.set_xticks(np.arange(np.min(x), np.max(x), 4))
ax_dire.set_xlabel("time in minutes")
ax_dire.legend()
