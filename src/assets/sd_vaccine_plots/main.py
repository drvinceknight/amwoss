from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')

def derivatives(t, y, vaccine_rate, birth_rate=0.01):
    """Defines the system of differential equations that
    describe the epidemiology model.

    Args:
        t: a positive float
        y: a tuple of three integers
        vaccine_rate: a positive float <= 1
        birth_rate: a positive float <= 1

    Returns:
        A tuple containing dS, dI, and dR
    """
    infection_rate = 0.3
    recovery_rate = 0.02
    death_rate = 0.01
    S, I, R = y
    N = S + I + R
    dSdt = (
        -((infection_rate * S * I) / N)
        + ((1 - vaccine_rate) * birth_rate * N)
        - (death_rate * S)
    )
    dIdt = (
        ((infection_rate * S * I) / N)
        - (recovery_rate * I)
        - (death_rate * I)
    )
    dRdt = (
        (recovery_rate * I)
        - (death_rate * R)
        + (vaccine_rate * birth_rate * N)
    )
    return dSdt, dIdt, dRdt

def integrate_ode(
    derivative_function,
    t_span,
    y0=(2999, 1, 0),
    vaccine_rate=0.85,
    birth_rate=0.01,
):
    """Numerically solve the system of differential equations.

    Args:
        derivative_function: a function returning a tuple
                             of three floats
        t_span: endpoints oif the time range to integrate over
        y0: a tuple of three integers (default: (2999, 1, 0))
        vaccine_rate: a positive float <= 1 (default: 0.85)
        birth_rate: a positive float <= 1 (default: 0.01)

    Returns:
        A tuple of three arrays
    """
    sol = solve_ivp(
        derivative_function,
        t_span,
        y0,
        args=(vaccine_rate, birth_rate),
    )
    ts, S, I, R = sol.t, sol.y[0], sol.y[1], sol.y[2]
    return ts, S, I, R

t_span = [0, 730]
t, S, I, R = integrate_ode(derivatives, t_span, vaccine_rate=0.0)

fig, ax = plt.subplots(1, figsize=(10, 5))
ax.plot(t, S, label='Susceptible', c='black', linestyle='solid', linewidth=1.75)
ax.plot(t, I, label='Infected', c='black', linestyle='dotted', linewidth=1.75)
ax.plot(t, R, label='Recovered', c='black', linestyle='dashed', linewidth=1.75)
ax.legend(fontsize=14, frameon=True, ncol=3, bbox_to_anchor=(0.85, 1.13))
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('People', fontsize=14)
fig.savefig("plot_no_vaccine.pdf")

t, S, I, R = integrate_ode(derivatives, t_span, vaccine_rate=0.85)

fig, ax = plt.subplots(1, figsize=(10, 5))
ax.plot(t, S, label='Susceptible', c='black', linestyle='solid', linewidth=1.75)
ax.plot(t, I, label='Infected', c='black', linestyle='dotted', linewidth=1.75)
ax.plot(t, R, label='Recovered', c='black', linestyle='dashed', linewidth=1.75)
ax.legend(fontsize=14, frameon=True, ncol=3, bbox_to_anchor=(0.85, 1.13))
ax.set_xlabel('Time', fontsize=14)
ax.set_ylabel('People', fontsize=14)
fig.savefig("plot_with_vaccine.pdf")