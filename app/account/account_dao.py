from sqlalchemy.orm import Session

from app.account.account import Account


def add(account: Account, session: Session):
    if account.id:
        session.merge(account)
    else:
        session.add(account)


def find_by_id(sub: str, session: Session) -> Account:
    account = session.query(Account).filter(Account.id == sub).first()
    return account


def find_by_email(email: str, session: Session) -> Account:
    return session.query(Account).filter(Account.email == email).first()
