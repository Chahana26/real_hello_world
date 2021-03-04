subroutine my_new_wrappers(x,y) bind(c)
   use iso_c_binding, only: c_int, c_double
   real(c_double), intent(in), value :: x,y
   call summation2(x,y)
end subroutine my_new_wrappers
