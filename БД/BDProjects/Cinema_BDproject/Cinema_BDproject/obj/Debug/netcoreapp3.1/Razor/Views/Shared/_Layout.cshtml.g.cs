#pragma checksum "/home/admin/Рабочий стол/Labs/БД/BDProjects/Cinema_BDproject/Cinema_BDproject/Views/Shared/_Layout.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "1fd9cc88d7830725f0eac8ade18378bcbe95de34"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Shared__Layout), @"mvc.1.0.view", @"/Views/Shared/_Layout.cshtml")]
namespace AspNetCore
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#nullable restore
#line 1 "/home/admin/Рабочий стол/Labs/БД/BDProjects/Cinema_BDproject/Cinema_BDproject/Views/_ViewImports.cshtml"
using Cinema_BDproject;

#line default
#line hidden
#nullable disable
#nullable restore
#line 2 "/home/admin/Рабочий стол/Labs/БД/BDProjects/Cinema_BDproject/Cinema_BDproject/Views/_ViewImports.cshtml"
using Cinema_BDproject.Models;

#line default
#line hidden
#nullable disable
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"1fd9cc88d7830725f0eac8ade18378bcbe95de34", @"/Views/Shared/_Layout.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"dd1c355c5948c75aace6af59c7842f497d1a2a30", @"/Views/_ViewImports.cshtml")]
    public class Views_Shared__Layout : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<dynamic>
    {
        #line hidden
        #pragma warning disable 0649
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperExecutionContext __tagHelperExecutionContext;
        #pragma warning restore 0649
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner __tagHelperRunner = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner();
        #pragma warning disable 0169
        private string __tagHelperStringValueBuffer;
        #pragma warning restore 0169
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __backed__tagHelperScopeManager = null;
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __tagHelperScopeManager
        {
            get
            {
                if (__backed__tagHelperScopeManager == null)
                {
                    __backed__tagHelperScopeManager = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager(StartTagHelperWritingScope, EndTagHelperWritingScope);
                }
                return __backed__tagHelperScopeManager;
            }
        }
        private global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.HeadTagHelper __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_HeadTagHelper;
        private global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.BodyTagHelper __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_BodyTagHelper;
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
            WriteLiteral("\n<!--\nAuthor: W3layouts\nAuthor URL: http://w3layouts.com\n-->\n<!doctype html>\n<html lang=\"zxx\">\n\n");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("head", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagAndEndTag, "1fd9cc88d7830725f0eac8ade18378bcbe95de343357", async() => {
                WriteLiteral("\n\t<!-- Required meta tags -->\n\t");
#nullable restore
#line 11 "/home/admin/Рабочий стол/Labs/БД/BDProjects/Cinema_BDproject/Cinema_BDproject/Views/Shared/_Layout.cshtml"
Write(await Html.PartialAsync("MetaTagsPartial"));

#line default
#line hidden
#nullable disable
                WriteLiteral("\n\t<!-- Template CSS -->\n\t");
#nullable restore
#line 13 "/home/admin/Рабочий стол/Labs/БД/BDProjects/Cinema_BDproject/Cinema_BDproject/Views/Shared/_Layout.cshtml"
Write(await Html.PartialAsync("CssPartial"));

#line default
#line hidden
#nullable disable
                WriteLiteral("\n\t<!-- Template CSS -->\n");
            }
            );
            __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_HeadTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.HeadTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_Razor_TagHelpers_HeadTagHelper);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral("\n\n");
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("body", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagAndEndTag, "1fd9cc88d7830725f0eac8ade18378bcbe95de344923", async() => {
                WriteLiteral("\n\n\t<!-- header -->\n\t");
#nullable restore
#line 20 "/home/admin/Рабочий стол/Labs/БД/BDProjects/Cinema_BDproject/Cinema_BDproject/Views/Shared/_Layout.cshtml"
Write(await Html.PartialAsync("HeaderPartial"));

#line default
#line hidden
#nullable disable
                WriteLiteral("\n\n\t<!-- //header -->\n\t");
#nullable restore
#line 23 "/home/admin/Рабочий стол/Labs/БД/BDProjects/Cinema_BDproject/Cinema_BDproject/Views/Shared/_Layout.cshtml"
Write(RenderBody());

#line default
#line hidden
#nullable disable
                WriteLiteral("\n");
                WriteLiteral("\t<!-- footer-66 -->\n\t");
#nullable restore
#line 26 "/home/admin/Рабочий стол/Labs/БД/BDProjects/Cinema_BDproject/Cinema_BDproject/Views/Shared/_Layout.cshtml"
Write(await Html.PartialAsync("FooterPartial"));

#line default
#line hidden
#nullable disable
                WriteLiteral("\n\t<!--//footer-66 -->\n");
            }
            );
            __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_BodyTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.BodyTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_Razor_TagHelpers_BodyTagHelper);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            WriteLiteral("\n\n</html>\n\t");
#nullable restore
#line 31 "/home/admin/Рабочий стол/Labs/БД/BDProjects/Cinema_BDproject/Cinema_BDproject/Views/Shared/_Layout.cshtml"
Write(await Html.PartialAsync("ScriptsPartial"));

#line default
#line hidden
#nullable disable
        }
        #pragma warning restore 1998
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<dynamic> Html { get; private set; }
    }
}
#pragma warning restore 1591
