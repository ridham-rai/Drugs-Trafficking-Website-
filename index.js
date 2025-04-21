const ctxActivity = document.getElementById('Activity_Chart').getContext('2d');
new Chart(ctxActivity, {
    type: 'line',
    data: {
        labels: ['2018', '2019', '2020', '2021', '2022', '2023'], // Yearly data
        datasets: [{
            label: 'Drug Cases Detected',
            data: [500, 700, 1200, 1500, 1800, 2200], // Example data
            borderColor: '#ff5722', // Line color
            borderWidth: 2,
            fill: false,
            pointBackgroundColor: '#ff5722',
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: true,
                position: 'top'
            },
            tooltip: {
                enabled: true,
                callbacks: {
                    label: function(tooltipItem) {
                        return `${tooltipItem.raw} cases`;
                    }
                }
            }
        },
        scales: {
            x: {
                title: {
                    display: true,
                    text: 'Year'
                }
            },
            y: {
                beginAtZero: true,
                title: {
                    display: true,
                    text: 'Number of Cases'
                }
            }
        }
    }
});
