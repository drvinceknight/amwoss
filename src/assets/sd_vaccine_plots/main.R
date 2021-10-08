library(deSolve)

#' Defines the system of differential equations that describe
#' the epidemiology model.
#'
#' @param t a positive float
#' @param y a tuple of three integers
#' @param vaccine_rate a positive float <= 1
#' @param birth_rate a positive float <= 1
#'
#' @return a list containing dS, dI, and dR
derivatives <- function(t, y, parameters){
  infection_rate <- 0.3
  recovery_rate <- 0.02
  death_rate <- 0.01
  with(as.list(c(y, parameters)), {
    N <- S + I + R
    dSdt <- ( - ( (infection_rate * S * I) / N)  # nolint
              + ( (1 - vaccine_rate) * birth_rate * N)
              - (death_rate * S))
    dIdt <- ( ( (infection_rate * S * I) / N)  # nolint
              - (recovery_rate * I)
              - (death_rate * I))
    dRdt <- ( (recovery_rate * I)  # nolint
              - (death_rate * R)
              + (vaccine_rate * birth_rate * N))
    list(c(dSdt, dIdt, dRdt))  # nolint
  })
}

#' Numerically solve the system of differential equations
#'
#' @param t an array of increasing positive floats
#' @param y0 list of integers (default: c(S=2999, I=1, R=0))
#' @param birth_rate a positive float <= 1 (default: 0.01)
#' @param vaccine_rate a positive float <= 1 (default: 0.85)
#'
#' @return a matrix of times, S, I and R values
solve_ode <- function(times,
                      y0 = c(S = 2999, I = 1, R = 0),
                      birth_rate = 0.01,
                      vaccine_rate = 0.84){
  params <- c(birth_rate = birth_rate,
              vaccine_rate = vaccine_rate)
  ode(y = y0,
      times = times,
      func = derivatives,
      parms = params)
}


times <- seq(0, 730, by = 0.01)
out <- solve_ode(times, vaccine_rate = 0.0)

pdf("plot_no_vaccine_R.pdf", width = 7, height = 5)
plot(out[, "time"], out[, "S"], type = "l", col = "blue")
lines(out[, "time"], out[, "I"], type = "l", col = "orange")
lines(out[, "time"], out[, "R"], type = "l", col = "darkgreen")
dev.off()



times <- seq(0, 730, by = 0.01)
out <- solve_ode(times, vaccine_rate = 0.85)

pdf("plot_with_vaccine_R.pdf", width = 7, height = 5)
plot(out[, "time"], out[, "S"], type = "l", col = "blue")
lines(out[, "time"], out[, "I"], type = "l", col = "orange")
lines(out[, "time"], out[, "R"], type = "l", col = "darkgreen")
dev.off()
