document.addEventListener('DOMContentLoaded', function () {
   // Fonction pour ouvrir le modal et définir l'ID de l'élève
   window.openModal = function (studentId) {
      const modal = document.getElementById('deleteModal');
      const confirmDeleteLink = document.getElementById('confirmDelete');

      // Mettre à jour le lien de suppression avec l'ID de l'élève
      confirmDeleteLink.href = `/student/delete/${studentId}/`;

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
