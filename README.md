# PyMinuitCKMFit
A Simple Script for Fitting Flavor Observables Using [iMinuit](https://iminuit.readthedocs.io/en/stable/).

## Useage
|Argument|Meaning|
|--------|-------|
|`-q`| Fit Quark sector, with delta CP in quark sector|
|`-l`| Fit lepton sector, must spesific ordering|
|`-NO`| Fit the neutrino masses with normal ordering|
|`-IO`| Fit the neutrino masses with inverted ordering|
|`-cd`| Fit the lepton sector with delta CP|
|`-s`| Use if the model use a see-saw mechanism for neutrino masses|
|`-m`| Use if you are using a modular flavor model (need to put modular form infor in `ModularForm.py`)|
|`-up [numbers]`| the upper bound of the parameters |
|`-low [numbers]`| the lower bound of the parameters |

### Examples
An example to fit the lepton sector with a model of see-saw mechanism, inverted ordering, with deltaCP phase in lepton sector, given the parameters are from 0.1 to 2:
```sh
python3 fit.py -l -IO -s -cp -up 2 -low 0.1 -f model/SimpleFNLepton/model1.py
```

An example to fit the quark sector given the parameters are from 0.1 to 2:
```sh
python3 fit.py -q -up 2 -low 0.1 -f model/QuarkModel.py
```

An example to fit both lepton and quark sector with a model of see-saw mechanism, normal ordering, with deltaCP phase in lepton sector, given the parameters are from 0.1 to 2:
```sh
python3 fit.py -q -l -NO -s -cp -up 2 -low 0.1 -f model/FlavorGW/model1.py
```

