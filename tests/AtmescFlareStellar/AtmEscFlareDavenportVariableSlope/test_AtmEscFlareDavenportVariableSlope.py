import astropy.units as u
from benchmark import Benchmark, benchmark


@benchmark(
    {
        "log.initial.system.Age": {"value": 3.1557600000e14, "unit": u.sec},
        "log.initial.system.Time": {"value": 0.0, "unit": u.sec},
        "log.initial.system.TotAngMom": {
            "value": 3.7230704732e41,
            "unit": (u.kg * u.m**2) / u.sec,
        },
        "log.initial.system.TotEnergy": {"value": -7.1876127212e39, "unit": u.Joule},
        "log.initial.star.Mass": {"value": 2.3860992000e29, "unit": u.kg},
        "log.initial.star.Radius": {"value": 3.1661898155e8, "unit": u.m},
        "log.initial.star.RadGyra": {"value": 0.4610332834},
        "log.initial.star.RotPer": {"value": 8.6400000000e4, "unit": u.sec},
        "log.initial.star.Luminosity": {
            "value": 6.5779241790e24,
            "unit": (u.kg * u.m**2) / u.sec**3,
        },
        "log.initial.star.LXUVStellar": {"value": 1.7103286997e-05, "unit": u.LSUN},
        "log.initial.star.LXUVFlare": {"value": 1.0944793096e-05, "unit": u.LSUN},
        "log.initial.star.Temperature": {"value": 3095.3300004448, "unit": u.K},
        "log.initial.star.FlareSlopeOUT": {"value": -0.7026960000},
        "log.initial.star.FlareYIntOUT": {"value": 22.1173920000},
        "log.final.system.Age": {"value": 3.4713360000e15, "unit": u.sec},
        "log.final.system.TotAngMom": {
            "value": 3.7295966219e41,
            "unit": (u.kg * u.m**2) / u.sec,
        },
        "log.final.system.TotEnergy": {"value": -7.1816302434e39, "unit": u.Joule},
        "log.final.star.Luminosity": {
            "value": 1.1827853786e24,
            "unit": (u.kg * u.m**2) / u.sec**3,
        },
        "log.final.star.LXUVStellar": {"value": 2.7351658447e-06, "unit": u.LSUN},
        "log.final.star.LXUVFlare": {"value": 3.4907273326e-06, "unit": u.LSUN},
        "log.final.star.Temperature": {"value": 3070.0997599141, "unit": u.K},
        "log.final.star.FlareSlopeOUT": {"value": -0.8575510923},
        "log.final.star.FlareYIntOUT": {"value": 27.0199563439},
    }
)
class Test_AtmEscFlareDavenportVariableSlope(Benchmark):
    pass
