import {Routes, RouterModule} from "@angular/router";
import {ModuleWithProviders} from "@angular/core";

import {HomeComponent} from "./home/components/home.component";

import {RegisterComponent} from "./register/components/register.component";
import {LoginComponent} from "./login/components/login.component";

import {MessageComponent} from "./Message/components/message.component";
import {SurveyComponent} from "./Survey/components/survey.component";

const appRoutes: Routes = [
    {path: '', redirectTo: 'home', pathMatch: 'full'},
    {path: 'home', component: HomeComponent, data: {title: 'Home'}},
    {path: 'register', component: RegisterComponent, data: {title: 'Register'}},
    {path: 'login', component: LoginComponent, data: {title: 'Login'}},
    {path: 'message', component: MessageComponent, data: {title: 'Message'}},
    {path: 'survey', component: SurveyComponent, data: {title: 'Survey'}}
];

export const appRoutingProviders: any[] = [];
export const routing: ModuleWithProviders = RouterModule.forRoot(appRoutes, { useHash: true });
