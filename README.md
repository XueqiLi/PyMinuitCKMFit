# PyMinuitCKMFit
A Simple Script for Fitting Flavor Observables Using [iMinuit](https://iminuit.readthedocs.io/en/stable/).

## Dependence
Please install `numpy`, `iminuit` to use it. If you need modular forms, you also need to install `mpmath`

## Useage
|Argument|Meaning|
|--------|-------|
|`-q`| Fit Quark sector, with delta CP in quark sector|
|`-l`| Fit lepton sector, must spesific ordering using `-NO` or `-IO`|
|`-NO`| Fit the neutrino masses with normal ordering|
|`-IO`| Fit the neutrino masses with inverted ordering|
|`-cd`| Fit the lepton sector with delta CP|
|`-s`| Use if the model use a see-saw mechanism for neutrino masses|
|`-m`| Use if you are using a modular flavor model (need to put modular form infor in `ModularForm.py`)|
|`-up [numbers]`| The fitting range of the parameters, the upper bound would be `low+up`, defult `20.0` |
|`-low [numbers]`| The lower bound of the parametersm defult `0.0` |
|`-mig [numbers]`| Number of `migrad` iteration, defult `100000` |
|`-scan [numbers]`| Number of initial points in the begining, around each point, a `migrad` fit will be proformed, defult `30` |
|`-itr [numbers]`| Number of iteration for further fit around the best fit point, defult `20` |

### Examples
An example to fit the quark sector:
```sh
 python3 fit.py -q -f model/QuarkModel.py
```

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
## Convention 
In our convention, the massmatrix should be derive as $\psi_i^L M_{ij} \bar{\psi}_j^R$, and the CKM matrix would be the matrix that relate the rand-handed fermion.