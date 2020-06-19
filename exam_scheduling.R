#' Writes the constraint row dealing with clashes
#'
#' @param clashes: a vector of module indicies that all cannot be scheduled at the same time
#' @param day: an integer representing the day
#'
#' @return the constraint row corresponding to that set of clashes on that day
write_Xclash_constraint_row_lhs <- function(clashes, day){
  row_lhs_Xday <- rep(0, n_modules)
  row_lhs_Xday[clashes] = 1
  row_lhs_Xnoday <- rep(0, n_modules)
  full_lhs_X <- append(append(rep(row_lhs_Xnoday, day - 1), row_lhs_Xday), rep(row_lhs_Xnoday, n_days-day))
  full_lhs <- append(full_lhs_X, rep(0, n_days))
  full_lhs
}



#' Writes the constraint row ensure every module is scheduled once
#'
#' @param module: an integer representing the module
#'
#' @return the constraint row corresponding to that set of scheduling to module on any day
write_Xreq_constraint_row_lhs <- function(module){
  row_lhs_day <- rep(0, n_modules)
  row_lhs_day[module] = 1
  full_lhs_X <- rep(row_lhs_day, n_days)
  full_lhs <- append(full_lhs_X, rep(0, n_days))
  full_lhs
}



#' Writes the constraint row representing the Y variable, whether at least one exam is scheduled on that day
#'
#' @param day: an integer representing the day
#'
#' @return the constraint row corresponding to creating Y
write_Y_constraint_row_lhs <- function(day){
  row_lhs_Xday <- rep(1, n_modules)
  row_lhs_Xnoday <- rep(0, n_modules)
  full_lhs_X <- append(append(rep(row_lhs_Xnoday, day - 1), row_lhs_Xday), rep(row_lhs_Xnoday, n_days-day))
  row_lhs_Y <- rep(0, n_days)
  row_lhs_Y[day] = -n_modules
  full_lhs <- append(full_lhs_X, row_lhs_Y)
  full_lhs
}



#' Writes all the constraints as a matrix, column of inequalities, and RHS column.
#'
#' @param list_of_clashes: a list of vectors corresponding to clashes, vectors of module indicies that all cannot be scheduled at the same time
#'
#' @return f.con the LHS of the constraints as a matrix
#' @return f.dir a vector of directions of the inequalities for each row of the constraints matrix
#' @return f.rhs a vector of LHS of the inequalities for each row of the constraints matrix
write_constraints <- function(list_of_clashes){
  all_rows <- c()
  all_dirs <- c()
  all_rhss <- c()
  n_rows <- 0
  
  for (clash in list_of_clashes){
    for (day in 1:n_days){
      row_lhs <- write_Xclash_constraint_row_lhs(clash, day)
      all_rows <- append(all_rows, row_lhs)
      
      all_dirs <- append(all_dirs, "<=")
      all_rhss <- append(all_rhss, 1)
      n_rows <- n_rows + 1
    }
  }
  
  for (module in 1:n_modules){
    row_lhs <- write_Xreq_constraint_row_lhs(module)
    all_rows <- append(all_rows, row_lhs)
    
    all_dirs <- append(all_dirs, "==")
    all_rhss <- append(all_rhss, 1)
    n_rows <- n_rows + 1
  }
  
  for (day in 1:n_days){
    row_lhs <- write_Y_constraint_row_lhs(day)
    all_rows <- append(all_rows, row_lhs)
    
    all_dirs <- append(all_dirs, "<=")
    all_rhss <- append(all_rhss, 0)
    n_rows <- n_rows + 1
  }
  
  f.con <- matrix(all_rows, nrow = n_rows, byrow = TRUE)
  f.dir <- all_dirs
  f.rhs <- all_rhss
  list(f.con, f.dir, f.rhs)
}



#' Writes the constraint row dealing with clashes
#'
#' @param n_modules: the number of modules to schedule
#' @param n_days: the maximum number of days to schedule (same as n_modules in worst case scenario)
#'
#' @return the objective function row to minimise
write_objective <- function(n_modules, n_days){
  obj <- c()
  num_zeros <- n_modules * n_days
  for (var in 1:num_zeros){
    obj <- append(obj, 0)
  }
  for (day in 1:n_days){
    obj <- append(obj, 1)
  }
  obj
}



# Now define the parameters, solve the problem
library(lpSolve)

n_modules = 26
n_days = 26

Ac <- c(1, 2, 3)
Ao <- c(4, 5, 6, 7, 8)
Bc <- c(9, 10, 11, 12, 13)
Bo <- c(14, 15, 16)
Cc <- c(17, 18, 19, 20)
Co <- c(21, 22)
Dc <- c(23, 24)
Do <- c(25, 26)

list_of_clashes <- list(
  c(Ac, Ao, Dc),
  c(Bc, Bo, Co),
  c(Bc, Bo, Ac),
  c(Cc, Co, Bo),
  c(Dc, Do)
)

constraints <- write_constraints(list_of_clashes = list_of_clashes)
f.con <- constraints[[1]]
f.dir <- constraints[[2]]
f.rhs <- constraints[[3]]
f.obj <- write_objective(n_modules = n_modules, n_days = n_days)


sol <- lp("min", f.obj, f.con, f.dir, f.rhs, all.bin = FALSE)  # Notice all.bin = FALSE. We need this to be TRUE, but it takes forever.

for (module in 1:n_modules){
  for (day in 1:n_days){
    var <- ((day - 1) * n_modules) + module
    if (sol$solution[var] == 1){
      print(c(module, day))
    }
  }
}




# See if we've defined the problem properly - see if the solution given by PuLP satisfies our constraints
solution_from_python <- c(0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 0.0)
                          
for (constraint_row in 1:182) {
  lhs <- sum(f.con[constraint_row,] * solution_from_python)
  sign <- f.dir[constraint_row]
  rhs <- f.rhs[constraint_row]
  expression <- paste(lhs, sign, rhs)
  if (!eval(parse(text=expression))) {
    print(constraint_row)
  }
}