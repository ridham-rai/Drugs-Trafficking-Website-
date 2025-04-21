const ctx = document.getElementById('Chart').getContext('2d');
        const trafficChart = new Chart(ctx, {
            type: 'pie',  // Change the chart type to pie
            data: {
                labels: ['Below 20 years', '21-30 years', '31-40 years', 'Above 40 years'],
                datasets: [{
                    label: 'Age Distribution of Drug Abusers',
                    data: [4.9, 36.9, 33.1, 25.1], // Data for age distribution
                    backgroundColor: ['skyblue', 'lightgreen', 'orange', 'salmon'],
                    borderColor: ['#fff', '#fff', '#fff', '#fff'],
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(tooltipItem) {
                                return tooltipItem.label + ': ' + tooltipItem.raw.toFixed(1) + '%';
                            }
                        }
                    }
                }
            }
        });

        // Map setup and markers (remains the same as the original code)
        const map = L.map('map').setView([20.5937, 78.9629], 5);

        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            maxZoom: 19,
            attribution: '&copy; OpenStreetMap contributors'
        }).addTo(map);

        const marker1 = L.marker([28.7041, 77.1025]).addTo(map).bindPopup('Suspicious activity reported here in Delhi.');
        const marker2 = L.marker([19.0760, 72.8777]).addTo(map).bindPopup('New report from Mumbai.');
        const marker3 = L.marker([13.0827, 80.2707]).addTo(map).bindPopup('Activity reported in Chennai.');