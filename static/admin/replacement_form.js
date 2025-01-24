document.addEventListener('DOMContentLoaded', function() {
    const buildingSelect = document.getElementById('id_buildings');
    const elevatorSelect = document.getElementById('id_elevator');

    if (buildingSelect && elevatorSelect) {
        buildingSelect.addEventListener('change', function() {
            const buildingId = buildingSelect.value;
            elevatorSelect.innerHTML = '';

            if (buildingId) {
                fetch(`/admin/lifts/building/${buildingId}/elevators/`)
                    .then(response => response.json())
                    .then(data => {
                        data.elevators.forEach(elevator => {
                            const option = document.createElement('option');
                            option.value = elevator.id;
                            option.textContent = elevator.elevator;
                            elevatorSelect.appendChild(option);
                        });
                    });
            }
        });
    }
});