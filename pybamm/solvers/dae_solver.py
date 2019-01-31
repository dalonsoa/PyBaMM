#
# Base solver class
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals


class DaeSolver(BaseSolver):
    """Solve a discretised model.

    Parameters
    ----------
    tolerance : float, optional
        The tolerance for the solver (default is 1e-8).
    """

    def __init__(self, tol=1e-8):
        super().__init__(tol)

    def solve(self, model, t_eval):
        """Calculate the solution of the model at specified times.

        Parameters
        ----------
        model : :class:`pybamm.BaseModel` (or subclass)
            The model whose solution to calculate. Must have attributes rhs and
            initial_conditions
        t_eval : numeric type
            The times at which to compute the solution

        """

        def residuals(t, y, ydot):
            return np.concatinate(
                model.concatenated_rhs.evaluate(t, y)-ydot,
                model.concatenated_residuals.evaluate(t, y)
            )

        y0 = model.concatenated_initial_conditions
        self.t, self.y = self.integrate(residuals, y0, t_eval)

    def integrate(self, residuals, y0, t_eval):
        """
        Solve a DAE model defined by residuals with initial conditions y0.

        Parameters
        ----------
        residuals : method
            A function that takes in t, y and ydot and returns the residuals of the
            equations
        y0 : numeric type
            The initial conditions
        t_eval : numeric type
            The times at which to compute the solution

        """
        raise NotImplementedError
