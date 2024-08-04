// Function to switch tabs
function go_to_step(number) {
    // Remove show active class from all tabs
    const tab1 = document.getElementById('tab1');
    const tab2 = document.getElementById('tab2');
    const tab3 = document.getElementById('tab3');

    tab1.classList.remove('show');
    tab1.classList.remove('active');
    tab2.classList.remove('show');
    tab2.classList.remove('active');
    tab3.classList.remove('show');
    tab3.classList.remove('active');

    // Show the respective tab
    const activeTab = `tab${number}`;
    document.getElementById(activeTab).classList.add('show');
    document.getElementById(activeTab).classList.add('active');
}