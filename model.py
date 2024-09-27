from scipy.integrate import odeint
import numpy as np


def ferm_ode(state, t, params):
    """Return the ODE as a function.

    The ODE is:
    dX/dt = mu * X * logistic inhibition based on pH
    dp/dt = 10**q * X * logistic inhibition based on pH

    Parameters:
    state = The pair of variables for the ODE:
            X is Bacterial concentration [1/L]
            p is Lactic acid concentration [mol/L]
    t = Time [hr]
    params = The ODE parameters (mu, q, c1 and c2) Refer to run_model
             function for the definitions of these.

    Outputs:
    f = The ODE as a function
    """
    X, p = state
    mu, q, c1, c2 = params # NB the order must match how params is set
    f = [mu * X * 1/(1 + np.exp(-c2 * (-np.log10(p) - c1))),
        10**q * X * 1/(1 + np.exp(-c2 * (-np.log10(p) - c1)))]
    return f


def run_model(mu, q, duration, state0):
    """Return the pH vs time curve as an ndarray.

    Parameters:
    mu = The bacterial concentration growth rate [1/hr]
    q = log10 of lactic acid concentration production rate /
            (bacteria / volume) [log10(mol/hr)]
    run_hrs = The time in hours to create the curve for.
    state0 = The initial state for the ODE, consisting of:
        1) X0 - The initial bacterial concentration [1/L]
        2) p0 - The initial lactic acid concentration [mol/L]

    Outputs:
    pH_curve = An ndarray consisting of one row for time in hours and one row
               for pH.
    """

    # Set ODE solver parameters (tuned by hand to get accurate results)
    abserr = 1.0e-8
    relerr = 1.0e-6

    run_hrs = np.arange(0, duration + 1.0 / 120.0, 1.0 / 120)
    # Use integrator to create the pH curve
    state_pred = odeint(ferm_ode, state0, run_hrs,
                        # NB params must be supplied as a tuple in this manner:
                        args=([mu, q, 5, 4/0.33],),
                        atol=abserr, rtol=relerr)
    pH_pred = [-np.log10(state[1]) for state in state_pred]

    # Put the predicted pH into an ndarray
    pH_curve = np.array([run_hrs, pH_pred])

    return pH_curve
