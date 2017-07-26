import { Injectable } from '@angular/core';
import { Http, Headers, Response } from '@angular/http';
import { Router } from '@angular/router';
import {BehaviorSubject} from 'rxjs/Rx';

import { LocalStorageService } from 'angular-2-local-storage';

@Injectable()
export class UserService {

  public isLoggedIn = new BehaviorSubject<boolean>(false);
  public user = new BehaviorSubject({});

  constructor(private http: Http, private localStorage: LocalStorageService, private router: Router) {
    this.isLoggedIn.next(!!localStorage.get('user'));
  }

  login(email, password) {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');


    return this.http
      .post(
      '/api/login',
      JSON.stringify({ email, password }),
      { headers }
      )
      .map(res => res.json())
      .map((res) => {
        this.isLoggedIn.next(true);
        this.user.next(res.result[0]);
        this.isLoggedIn.next(true);
        this.localStorage.set('logged_in', 'true');
      });
  }

  getCurrentUser() {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');

    // this.isLoggedIn.next(true);

    return this.http
      .get(
      '/api/current_user'
      ).map(res => res.json());
  }

  logout() {
      console.log("in userService logout\n");
      this.isLoggedIn.next(false);
    this.http.get('/api/logout').subscribe();
    this.router.navigate(['home']);
  }
  //
  // sendMessage(id, mess, pushTime) {
  //   let headers = new Headers();
  //   headers.append('Content-Type', 'application/json');
  //
  //
  //   return this.http
  //     .post(
  //     '/api/message',
  //     JSON.stringify({ id, mess, pushTime }),
  //     { headers }
  //     )
  //     .map(res => res.json());
  // }
  // getMessages() {
  //   let headers  = new Headers();
  //   headers.append('Content-Type', 'application/jason');
  //
  //   return this.http
  //     .get(
  //     '/api/readmessages'
  //     )
  //     .map(res => res.json());
  // }
  //
  // sendQuestion(id, quest, qtype, pushTime) {
  //   let headers = new Headers();
  //   headers.append('Content-Type', 'application/json');
  //
  //
  //   return this.http
  //     .post(
  //     '/api/question',
  //     JSON.stringify({ id, quest, qtype, pushTime }),
  //     { headers }
  //     )
  //     .map(res => res.json());
  // }
  //
  // getQuestions() {
  //   let headers  = new Headers();
  //   headers.append('Content-Type', 'application/jason');
  //
  //   return this.http
  //     .get(
  //     '/api/readquestions'
  //     )
  //     .map(res => res.json());
  // }
}
