using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.AspNetCore.Mvc.Rendering;
using DollarsAndSenseFCS.Data;
using DollarsAndSenseFCS.Models;

namespace DollarsAndSenseFCS.Pages.Contact
{
    public class CreateModel : PageModel
    {
        private readonly DollarsAndSenseFCS.Data.DollarsAndSenseFCSContext _context;

        public CreateModel(DollarsAndSenseFCS.Data.DollarsAndSenseFCSContext context)
        {
            _context = context;
        }

        public IActionResult OnGet()
        {
            return Page();
        }

        [BindProperty]
        public Contact Contact { get; set; }

        // To protect from overposting attacks, see https://aka.ms/RazorPagesCRUD
        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            _context.Contact.Add(Contact);
            await _context.SaveChangesAsync();

            return RedirectToPage("./Index");
        }
    }
}
