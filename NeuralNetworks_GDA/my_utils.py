def get_mu(data, _class):
    data = data.where(data['class'] == _class)
    return data.loc[:, :].mean()

