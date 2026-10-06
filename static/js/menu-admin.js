document.addEventListener('DOMContentLoaded', () => {
  const select = document.getElementById('id_destination_type');
  if (!select) return;

  const fields = {
    route: document.querySelector('.field-route_name'),
    page: document.querySelector('.field-page'),
    external: document.querySelector('.field-external_url'),
  };

  const update = () => {
    for (const [type, row] of Object.entries(fields)) {
      if (row) row.hidden = select.value !== type;
    }
  };

  select.addEventListener('change', update);
  update();
});
