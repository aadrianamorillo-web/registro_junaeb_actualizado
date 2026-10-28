// Pequeñas mejoras de interacción para la página de asistencia.
document.addEventListener("DOMContentLoaded", () => {
  const fecha = document.querySelector('input[name="fecha"]');
  if (fecha) {
    fecha.addEventListener("change", () => {
      // El formulario de filtros permite consultar la asistencia de otra fecha.
      fecha.form?.requestSubmit();
    });
  }
});
