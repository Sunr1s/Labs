using Cinema_BDproject.Domain;
using Cinema_BDproject.Domain.Repositories;
using Cinema_BDproject.Domain.Repositories.Abstract;
using Cinema_BDproject.Domain.Repositories.MongoFramework;
using Cinema_BDproject.Models;
using Cinema_BDproject.Services;
using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.HttpsPolicy;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.Options;
using MongoDB.Driver;
using System;

namespace Cinema_BDproject
{
    public class Startup
    {
        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }

        public IConfiguration Configuration { get; }

        // This method gets called by the runtime. Use this method to add services to the container.
        public void ConfigureServices(IServiceCollection services)
        {
            //подключаем конфиг из appsetting.json
            Configuration.Bind("Project", new Config());
            Configuration.Bind("MongoDbConfig", new MongoDbConfig());
            //подключаем нужный функционал приложения в качестве сервисов
            services.Configure<MongoDbConfig>(
              Configuration.GetSection(nameof(MongoDbConfig)));

            services.AddSingleton<IMongoDbConfig>(sp =>
                sp.GetRequiredService<IOptions<MongoDbConfig>>().Value);

            services.AddScoped<ITextFieldsRepos, TextFieldRepos>();
            services.AddTransient<IServiceItemRepos, ServiceRepos>();
            services.AddTransient<DataManager>();

            //подключаем контекст БД 
            var mongoDbSettings = Configuration.GetSection(nameof(MongoDbConfig)).Get<MongoDbConfig>();


            // Add services to the container.
            services.AddSingleton<IMongoClient, MongoClient>(sp => new MongoClient(mongoDbSettings.ConnectionString));

            services.AddIdentity<ApplicationUser, ApplicationRole>()
                .AddMongoDbStores<ApplicationUser, ApplicationRole, Guid>
                (
                   mongoDbSettings.ConnectionString, mongoDbSettings.Name
                );
            //настраиваем authentication cookie
            services.ConfigureApplicationCookie(options =>
            {
                options.Cookie.Name = "myCompanyAuth";
                options.Cookie.HttpOnly = true;
                options.LoginPath = "/account/login";
                options.AccessDeniedPath = "/account/accessdenied";
                options.SlidingExpiration = true;
            });

            //настраиваем политику авторизации для Admin area
            //services.AddAuthorization(x =>
            //{
            //    x.AddPolicy("AdminArea", policy => { policy.Rol("admin"); });
            //});
            services.AddControllersWithViews(x =>
            {
                //x.Conventions.Add(new AdminAreaAutorisation("Admin", "AdminArea"));
            })
                //выставляем совместимость с asp.net core 3.0
                .SetCompatibilityVersion(CompatibilityVersion.Version_3_0).AddSessionStateTempDataProvider();
  

        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }
            else
            {
                app.UseExceptionHandler("/Home/Error");
                // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
                app.UseHsts();
            }
            app.UseHttpsRedirection();
            app.UseStaticFiles();

            app.UseRouting();

            app.UseAuthentication();
            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllerRoute("admin", "{area:exists}/{controller=Home}/{action=Index}/{id?}");
                endpoints.MapControllerRoute(
                    name: "default",
                    pattern: "{controller=Home}/{action=Index}/{id?}");
               
            });
        }
    }
}
