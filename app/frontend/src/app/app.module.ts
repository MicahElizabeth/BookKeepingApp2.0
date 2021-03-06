import {NgModule}      from '@angular/core';
import {BrowserModule} from '@angular/platform-browser';

import {AppComponent} from "./app.component";
import {NavComponent} from "./layout/navbar/navbar.component";
import {FooterComponent} from "./layout/footer/footer.component";

import {HomeComponent} from "./home/components/home.component";

import {RegisterComponent} from "./register/components/register.component";
import {LoginComponent} from "./login/components/login.component";
import {UserService} from "./user/services/user.service";

import {routing, appRoutingProviders} from './app.routing';
import {FormsModule} from '@angular/forms';

import {HttpModule}    from '@angular/http';
import {LocalStorageModule} from 'angular-2-local-storage';

@NgModule({
    imports: [
        BrowserModule,
        HttpModule,
        FormsModule,
        HttpModule,
        routing,
        LocalStorageModule.withConfig({prefix: 'app', storageType: 'sessionStorage'})
    ],
    declarations: [
        AppComponent,
        HomeComponent,
        RegisterComponent,
        NavComponent,
        FooterComponent,
        LoginComponent
    ],
    providers: [
        appRoutingProviders,
        UserService
    ],
    bootstrap: [AppComponent]
})
export class AppModule {
}
