document.addEventListener('DOMContentLoaded', function () {
   // Fonction pour ouvrir le modal et définir l'ID du professeur
   window.openModal = function (teacherId) {
      const modal = document.getElementById('deleteModal');
      const confirmDeleteLink = document.getElementById('confirmDelete');

      // Mettre à jour le lien de suppression avec l'ID du professeur
      confirmDeleteLink.href = `/teacher/delete/${teacherId}/`; // Assurez-vous que l'URL est correcte

      if (modal) {
         modal.classList.remove('hidden');
      }
   };

   // Fonction pour fermer le modal
   window.closeModal = function () {
      const modal = document.getElementById('deleteModal');
      if (modal) {
         modal.classList.add('hidden');
      }
   };
});
